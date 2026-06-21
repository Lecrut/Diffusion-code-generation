if __name__ == '__main__':
    fruits = {"apple": "red", "banana": "yellow", "kiwi": "green"}
    longest_fruit = max(fruits, key=len)
    print(longest_fruit)