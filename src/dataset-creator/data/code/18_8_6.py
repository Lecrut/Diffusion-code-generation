if __name__ == '__main__':
    fruit_list = ["apple", "banana", "orange", "grape", "strawberry", "mango", "pineapple"]
    fruit_types = {fruit: "sweet" for fruit in fruit_list if fruit in ["apple", "banana", "orange", "grape", "strawberry", "mango"]}
    print(fruit_types)