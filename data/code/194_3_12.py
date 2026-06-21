if __name__ == '__main__':
    fruits = {"apple": "fruit", "banana": "fruit", "kiwi": "fruit", "orange": "fruit"}
    longest_fruit = max(fruits, key=len)
    print(longest_fruit)