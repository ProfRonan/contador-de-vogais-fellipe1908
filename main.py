"""This program counts the number of vowels in a string."""


def count_vowels(string:str) -> int:
    quant = 0
    for c in string:
        if c in "aeiou" or c in "AEIOU ":
            quant += 1
    return quant

if __name__ == "__main__":
    count_vowels("")
