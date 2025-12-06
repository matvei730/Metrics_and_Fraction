class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def plus(self, fraction_two):
        new_numerator = self.numerator * fraction_two.denominator + fraction_two.numerator * self.denominator
        new_denominator = self.denominator * fraction_two.denominator
        return Fraction(new_numerator, new_denominator)

    def mines(self, fraction_two):
        new_numerator = self.numerator * fraction_two.denominator - fraction_two.numerator * self.denominator
        new_denominator = self.denominator * fraction_two.denominator
        return Fraction(new_numerator, new_denominator)

    def division(self, fraction_two):
        new_numerator = self.numerator * fraction_two.denominator
        new_denominator = self.denominator * fraction_two.numerator
        return Fraction(new_numerator, new_denominator)

    def multiplication(self, fraction_two):
        new_numerator = self.numerator * fraction_two.numerator
        new_denominator = self.denominator * fraction_two.denominator
        return Fraction(new_numerator, new_denominator)

    def new_numerator(self, numerator):
        self.numerator = numerator

    def new_denominator(self, denominator):
        self.denominator = denominator

    def display_fraction(self):
        return f"{self.numerator}/{self.denominator}"

    def return_numerator(self):
        return self.numerator

    def return_denominator(self):
        return self.denominator


class Conversion:
    @staticmethod
    def celsius_in_fahrenheit(celsius):
        return celsius * 1.8 + 32

    @staticmethod
    def fahrenheit_in_celsius(fahrenheit):
        return (fahrenheit - 32) * 1.8


class Translation:

    @staticmethod
    def kilometer_in_miles(kilometer):
        return kilometer * 0.621371

    @staticmethod
    def miles_in_kilometer(miles):
        return miles / 0.621371

    @staticmethod
    def halon_in_liter(liter):
        return liter * 4.546

    @staticmethod
    def liter_in_halon(halon):
        return halon / 4.546
g = Translation()
g.liter_in_halon()