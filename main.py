class Library:
    def __init__(self):
        self.file_name = "kitaplar.txt"
        self.books = []

        try:
            with open(self.file_name, "a+") as file:
                file.close()
        except FileNotFoundError:
            print(f"{self.file_name} dosyası bulunamadı.")

    def list_books(self):
        try:
            with open(self.file_name, "r") as file:
                lines = file.read().splitlines()
                for line in lines:
                    book_info = line.split(', ')
                    print(f"Kitap Adı: {book_info[0]}, Yazar: {book_info[1]}")
        except FileNotFoundError:
            print(f"{self.file_name} dosyası bulunamadı.")

    def add_book(self):
        title = input("Kitap Adı: ")
        author = input("Yazar: ")
        publication_year = input("Yayın Tarihi: ")
        page_count = input("Sayfa Sayısı: ")

        new_book = f"{title}, {author}, {publication_year}, {page_count}"

        try:
            with open(self.file_name, "a") as file:
                file.write(new_book + "\n")
                print("Kitap başarıyla eklendi.")
        except FileNotFoundError:
            print(f"{self.file_name} dosyası bulunamadı.")

    def remove_book(self):
        title_to_remove = input("Kaldırılacak Kitap Adı: ")

        try:
            with open(self.file_name, "r") as file:
                lines = file.read().splitlines()
                books = [line.split(', ') for line in lines]

                for i, book in enumerate(books):
                    if book[0] == title_to_remove:
                        del books[i]
                        break

            with open(self.file_name, "w") as file:
                for book in books:
                    file.write(", ".join(book) + "\n")

            print(f"{title_to_remove} adlı kitap başarıyla kaldırıldı.")
        except FileNotFoundError:
            print(f"{self.file_name} dosyası bulunamadı.")


# Ana program
lib = Library()

while True:
    print("*** MENÜ ***")
    print("1) Kitapları Listeleyin")
    print("2) Kitap Ekle")
    print("3) Kitabı Kaldır")
    print("4) Çıkış")

    choice = input("Seçiminiz (1-4): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
