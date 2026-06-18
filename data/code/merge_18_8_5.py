if __name__ == '__main__':
    fruit_list = ["apple", "banana", "orange", "grape", "strawberry", "mango", "pineapple"]
    fruit_types = {fruit: "berry" if fruit in ["strawberry", "grape"] else ("citrus" if fruit in ["orange"] or fruit in ["pineapple"] else "other") for fruit in fruit_list}
    print(fruit_types)