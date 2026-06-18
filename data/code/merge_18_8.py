if __name__ == '__main__':
    fruit_list = ["apple", "banana", "orange", "grape", "strawberry", "mango", "pineapple"]
    fruit_types = {fruit: "sweet" for fruit in fruit_list if fruit in ["apple", "banana", "orange", "grape", "mango"]}
    fruit_types.update({fruit: "tart" for fruit in fruit_list if fruit in ["strawberry", "pineapple"]})
    fruit_types.update({fruit: "citrus" for fruit in fruit_list if fruit in ["orange"]})
    print(fruit_types)