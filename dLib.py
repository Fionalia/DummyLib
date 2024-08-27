import sys

# class containing methods to modify existing methods and new methods to modify string variables
class text:

    # built-in print() method replacement, outputting text 1 character at a time
    def dPrint(self, text):
        text = str(text)
        for x in text:
            sys.stdout.write(x)
        sys.stdout.write("\n")

# class containing methods to replace existing math operations
class math:

    # NOTE: I do not really understand the entirety of bitwise mathematics. Anything after addition is where I nope out. I required some help from an AI friend for the rest of the bitwise things

    # private method to add numbers using bitwise operations
    def __add(self, a, b):
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a
    
    # private method to subtract numbers using bitwise operations
    def __sub(self, a, b):
        while b != 0:
            carry = (~a) & b
            a = a ^ b
            b = carry << 1
        return a  

    # adds numbers by increasing the value of the first given by 1 repeatedly
    def dAdd(self, *nums):
        total = 0
        for x in nums:
            total = self.__add(x, total)
        return total
    
    # subtracts all numbers from the first given argument `fnum`. Does not work with all number combinations
    def dSub(self, fnum, *nums):
        res = fnum
        for num in nums:
            res = self.__sub(res, num)
        return res