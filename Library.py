class IdError(Exception):
	'''
CUSTOMIZED EXCEPTION CLASS
It throws an error when the ID provided is not valid
	'''
	pass

class ApartmentError(Exception):
	'''
CUSTOMIZED EXCEPTION CLASS
It throws an error when the apartment provided is not valid
	'''
	pass

class StockError(Exception):
	'''
CUSTOMIZED EXCEPTION CLASS
It throws an error when the stock provided is not valid
	'''
	pass


class Library :
	'''
	INSTANTIATION FOR A LIBRARY OBJECT
	This is an OOP project for a library where you can borrow, access and return books,
	 then the library workers too can check for remaining stock,
	 check for availabily of books and verify your IDsB
	'''

	MIN_STOCK = 0 # <-- class level attribute

	def __init__(self, department, apartment = None, stock = [], available_books = [],
	 not_available = [], returned_book = [], remaining_stock = 0, id = None, book_borrowed = [],
	  count_order = 0):# <-- Initialization method For setting and getting attributes
		self._borrowed_book = book_borrowed # <-- Instance Level attributes
		self._department = department
		self._apartment = apartment
		self._stock = stock
		self._id = id
		self._count_order = count_order

		self._remaining_stock = remaining_stock
		self._available_books = available_books
		self._not_available = not_available
		self._returned_book = returned_book
		self._total_stock = 0
		
		for i in self._returned_book: 
			if self._returned_book is None:
				self._remaining_stock = self._remaining_stock + 0
				
			else :
				self._remaining_stock = self._remaining_stock + 1
		for i in self._borrowed_book:
			if self._borrowed_book == None :
				self._count_order += 0
				self._total_remaining = self._remaining_stock - 0
			else :
				self._count_order += 1
				self._remaining_stock = self._remaining_stock - 1
	
	@property
	def total_stock(self):
		return self._total_stock
	@total_stock.setter
	def total_stock(self, total):
		if total < 0 :
			raise StockError ("Stock cant be a negative number")
		self._total_stock = total

		
		
	def borrow_book(self): # <-- Instance level Methods,  Displays books to borrow
		return"The book you borrowed is {}".format(self._borrowed_book)


	def return_book (self): # Displays books being returned
		return "The book you returned is {}".format(self._returned_book)

	@property
	def access_book (self): # <-- Read only setter method, helps to access books
		if self._department[0].upper() in ["A","B","C","D","E","F","G"]:
			self._apartment = "Main floor"
			if self._department[0].upper() == "A":
				shelf = "First shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "B":
				shelf = "Second shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "C":
				shelf = "Third shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "D":
				shelf = "Fourth shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "E":
				shelf = "Fifth shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "F":
				shelf = "Sixth shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "G":
				shelf = "Seventh shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
		elif self._department[0].upper() in ["H","I","J","K","L","M","N"]:
			self._apartment = "Top floor"
			if self._department[0].upper() == "H":
				shelf = "First shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "I":
				shelf = "Second shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "J":
				shelf = "Third shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "K":
				shelf = "Fourth shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "L":
				shelf = "Fifth shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "M":
				shelf = "Sixth shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "N":
				shelf = "Seventh shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
		
		elif self._department[0].upper() in ["O","P","Q","R","S","T","U"]:
			self._apartment = "Basement"
			if self._department[0].upper() == "O":
				shelf = "First shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "P":
				shelf = "Second shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "Q":
				shelf = "Third shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "R":
				shelf = "Fourth shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "S":
				shelf = "Fifth shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "T":
				shelf = "Sixth shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "U":
				shelf = "Seventh shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
		elif self._department[0].upper() in ["V","W","X","Y","Z"]:
			self._apartment = "Extended floor"
			if self._department[0].upper() == "V":
				shelf = "First shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "W":
				shelf = "Second shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "X":
				shelf = "Third shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "Y":
				shelf = "Fourth shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			elif self._department[0].upper() == "Z":
				shelf = "Fifth shelf"
				return "Go to the {} and check the {} ".format(self._apartment, shelf)
			

		else:
			raise ApartmentError ("Apartment only takes string values") # <-- Throw an exception if the condition is met.

class Admin(Library):
	'''
INSTANTIATION OF THE ADMIN PART OF THE LIBRARY
This is the administrative part of the library, it inherits from class Library 
that will verify IDs, checks books remaining, check stocks
	'''
	@property
	def check_borrowed (self): # method to check for borrowed books

		for i in self._borrowed_book:

			if i in  self._stock :
				self._available_books.append(i)
				self._stock.remove(i)
			else :
				self._not_available.append(i)
		return "Total available books are {}, while {} are not available".format(self._available_books, self._not_available)

	def __eq__(self, other):
		self._id == other._id
		raise IdError ("Id is taken already")
		
	def check_id (self): # Method to check IDs
		if self._id == None :
			raise IdError("Invalid ID")
		else:
			return "Your ID is {}".format(self._id)
	@property
	def count_remaining (self): # Method to counts for books remaining
		if self._remaining_stock < Library.MIN_STOCK :
			raise StockError("Remaining stock can't have a negative value")
		return "The total book remaining is {}".format(self._remaining_stock)


help(Library)