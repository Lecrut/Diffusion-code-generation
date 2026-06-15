if __name__ == '__main__':
    fruit_list = ["apple", "banana", "carrot", "grape", "orange", "strawberry", "melon"]
    fruit_types = {fruit: "sweet" if fruit in ["apple", "banana", "grape", "strawberry"] else ("root" if fruit == "carrot" else ("citrus" if fruit in ["orange"] else "other")) for fruit in fruit_list}
    print(fruit_types)