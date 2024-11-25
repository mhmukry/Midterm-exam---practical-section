

class bookStore:
    def __init__(self, store_name, total_number_of_books_available, number_of_available_books, rental_fee_per_book, late_fee_per_day):
        self.store_name = store_name
        self.total_number_of_books_available = total_number_of_books_available
        self.number_of_books_available = number_of_available_books
        self.rental_fee_per_book = rental_fee_per_book
        self.late_fee_per_day = late_fee_per_day








    def get_store_name(self):
        return self.store_name

    def set_store_name(self, store_name):
        self.store_name = store_name


    def get_total_number_of_books_available(self):
        return self.total_number_of_books_available
    
    def set_total_number_of_books_available(self, total_number_of_books_available):
        return self.total_number_of_books_available = total_number_of_books_available
    

    def get_number_of_available_books(self):
        return self.number_of_available_books 
    
    def set_number_of_available_books(self, number_of_available_books):
        return self.number_of_available_books = number_of_available_books
    

    def get_rental_fee_per_book(self):
        return self.rental_fee_per_book
    
    def set_rental_fee_per_book(self, rental_fee_per_book):
        return self.rental_fee_per_book = rental_fee_per_book
