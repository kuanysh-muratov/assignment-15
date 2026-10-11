from random import shuffle, randint
from math import pi
"""
Exercise 1:
Create a Pizza class that could have ingredients added to it. Raise an error if an attempt is made to add a duplicate ingredient.
"""
class Pizza:
    def __init__(self):
        self.ingredients = []
    
    def add_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            raise ValueError('The ingredients has already been added')
        self.ingredients.append(ingredient)


"""
Exercise 2:
Create an Elevator class with methods to go up, go down, and get the current floor. The elevator should not be able to go below the ground floor (floor 0).
"""
class Elevator:
    def __init__(self):
        self.floor = 0

    def go_up(self):
        self.floor += 1

    def go_down(self):
        if self.floor:
            self.floor -= 1

    def get_current_floor(self):
        return self.floor


"""
Exercise 3:
Create a class Stack with methods to push, pop, and check if the stack is empty. 
Raise an exception if a pop is attempted on an empty stack.
"""
class Stack:
    def __init__(self):
        self.__contents = []

    def push(self, item):
        self.__contents.append(item)

    def pop(self):
        return self.__contents.pop()

    def is_empty(self):
        return len(self.__contents) == 0


"""
Exercise 4:
Design a BankAccount class with methods to deposit, withdraw, and check balance. Ensure that an account cannot go into a negative balance.
"""
class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError('Not enough balance')
        self._balance -= amount

    def check_balance(self):
        return self._balance


"""
Exercise 5:
Create a class Person with attributes for name and age. 
Implement a method birthday that increases the person's age by one. Raise an exception if an age less than 0 is entered.
"""
class Perrson:
    def __init__(self, name, age):
        self.name = name

        if age < 0:
            raise ValueError('Age must be non-negative')
        
        self.age = age

    def birthday(self):
        self.age += 1


"""
Exercise 6:
Create an Animal base class and a Dog and Cat derived classes. Each animal should have a sound method which returns the sound they make.
"""
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return 'Woof'

class Cat(Animal):
    def sound(self):
        return 'Meow'


"""
Exercise 7:
Design a class Calculator with static methods for addition, subtraction, multiplication, and division. Division method should raise a ZeroDivisionError when trying to divide by zero.
"""
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x / y


"""
Exercise 8:
Create a class `Car` with attributes for speed and mileage. 
Raise a ValueError if a negative value for speed or mileage is entered.
"""
class Car:
    def __init__(self, speed, mileage):
        if speed < 0 or mileage < 0:
            raise ValueError()
        self.speed, self.mileage = speed, mileage


"""
Exercise 9:
Create a Student class and a Course class. Each Course can enroll students and print a list of enrolled students.
"""
class Studennt:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self):
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def print_students(self):
        print(*self.students)


"""
Exercise 10:
Create a Flight class with a destination, departure time, and a list of passengers. Implement methods to add passengers, change the destination, and delay the flight by a certain amount of time.
"""
class Flight:
    def __init__(self, destination, departure):
        self.destination = destination
        self.departure = departure
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def change_destination(self, new_destination):
        self.destination = new_destination

    def delay(self, delay_time):
        dh = int(delay_time)
        dm = int((delay_time - dh) * 60)
        h, m = map(int, self.departure.split(':'))
        r, m = divmod(m + dm, 60)
        h = (h + dh + r) % 24
        self.departure = f'{h:02d}:{m:02d}'

"""
Exercise 11:
Create a Library class with a list of Book objects. 
The Book class should have attributes for title and author. 
The Library class should have methods to add books and find a book by title.
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


"""
Exercise 12:
Design a class Matrix that represents a 2D matrix with methods for addition, subtraction, and multiplication. 
Implement error handling for operations that are not allowed (e.g., adding matrices of different sizes).
"""
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __check_sizes(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise TypeError('Matrices are of incompatible sizes')
        
    def add(self, other):
        self.__check_sizes(other)
        return Matrix([[self.matrix[row][col] + other.matrix[row][col] for col in range(len(self.matrix[0]))] 
                for row in range(len(self.matrix))])

    def subtract(self, other):
        self.__check_sizes(other)
        return Matrix([[self.matrix[row][col] - other.matrix[row][col] for col in range(len(self.matrix[0]))] 
                        for row in range(len(self.matrix))])

    def multiply(self, other):
        self.__check_sizes(other)
        return Matrix([[self.matrix[row][col] - other.matrix[row][col] for col in range(len(self.matrix[0]))] 
                for row in range(len(self.matrix))])


"""
Exercise 13:
Create a class Rectangle with attributes for height and width. Implement methods for calculating the area and perimeter of the rectangle. Also, implement a method is_square that returns true if the rectangle is a square and false otherwise.
"""
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def is_square(self):
        return self.height == self.width


"""
Exercise 14:
Design a class Circle with attributes for radius. Implement methods for calculating the area and the circumference of the circle. Handle exceptions for negative radius values.
"""
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * pow(self.radius, 2)

    def circumference(self):
        return 2 * pi * self.radius


"""
Exercise 15:
Design a class Triangle with methods to calculate the area and perimeter. 
Implement error handling for cases where the given sides do not form a valid triangle.
"""
class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if not (side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_a + side_b):
            raise ValueError('Invalid triangle')
        self.side_a, self.side_b, self.side_c = side_a, side_b, side_c

    def area(self):
        p = self.perimeter() / 2
        return pow(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c), 0.5)

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


"""
Exercise 17:
Create a MusicPlayer class that contains a list of songs and methods to add songs, play a song, and skip to the next song. 
Also implement a method to shuffle the playlist.
"""
class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self._idx = 0
        self.current_song = None

    def add_song(self, song):
        self.playlist.append(song)
        if self.current_song is None:
            self.current_song = song

    def play_song(self):
        if not self.playlist:
            print('Your playlist is empty')
        else:
            print(f'Playing {self.current_song}')

    def next_song(self):
        if not self.playlist:
            return
        self._idx += 1
        self._idx %= len(self.playlist)
        self.current_song = self.playlist[self._idx]
        
    def shuffle(self):
        shuffle(self.playlist)


"""
Exercise 18:
Design a Product class for an online store with attributes for name, price, and quantity. 
Implement methods to add stock, sell product, and check stock levels. 
Include error handling for attempting to sell more items than are in stock.
"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, quantity):
        self.quantity += quantity

    def sell(self, quantity):
        if quantity > self.quantity:
            raise ValueError()
        self.quantity -= quantity

    def check_stock(self):
        return self.quantity


"""
Exercise 19:
Create a VideoGame class with attributes for title, genre, and rating. Implement methods to change the rating, change the genre, and display game details.
"""
class VideoGame:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def change_rating(self, rating):
        self.rating = rating

    def change_genre(self, genre):
        self.genre = genre

    def display_details(self):
        return f'{self.title} - {self.genre} ({self.rating})'


"""
Exercise 20:
Create a School class with a list of Teacher and Student objects. 
Teacher and Student classes should have attributes for name and age. 
The School class should have methods to add teachers, add students, and print a list of all people in the school.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    pass

class Student(Person):
    pass

class School:
    def __init__(self):
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def get_all(self):
            return *self.teachers, *self.students

    def print_all(self):
        print(*self.get_all())


"""
Exercise 21:
Design a Card class to represent a playing card with suit and rank.
Then design a Deck class that uses the Card class.
The Deck class should have methods to shuffle the deck, deal a card, and check the number of remaining cards.
"""
class Card:
    SUITS = ('♠', '♥', '♦', '♣')
    RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self):
        self.__cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]

    def shuffle(self):
        shuffle(self.__cards)

    def deal(self):
        if self.count() == 0:
            print('No card left to deal')
            return
        rand_idx = randint(0, self.count() - 1)
        return self.__cards.pop(rand_idx)

    def count(self):
        return len(self.__cards)
