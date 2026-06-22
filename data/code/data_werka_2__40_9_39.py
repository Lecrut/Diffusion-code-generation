def get_first_letters(strings):
    return [s[0] for s in strings if s]

if __name__ == '__main__':
    fruits = ["strawberry", "watermelon", "pineapple", "lemon"]
    first_letters = get_first_letters(fruits)
    print(first_letters)

    vegetables = ["carrot", "broccoli", "spinach", "asparagus"]
    vegetable_initials = get_first_letters(vegetables)
    print(vegetable_initials)