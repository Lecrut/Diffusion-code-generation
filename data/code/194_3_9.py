if __name__ == '__main__':
    fruits = {"apple": 5, "banana": 6, "kiwi": 4, "orange": 6}
    longest_fruit = max(fruits, key=fruits.get)
    print(longest_fruit)