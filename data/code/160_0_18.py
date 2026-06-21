def manage_fruit_list():
    fruits = ['apple', 'banana', 'orange']
    
    def add_fruit(fruit):
        if fruit not in fruits:
            fruits.append(fruit)
            print(f"Added {fruit}")
        else:
            print(f"{fruit} already exists")
    
    def remove_fruit(fruit):
        if fruit in fruits:
            fruits.remove(fruit)
            print(f"Removed {fruit}")
        else:
            print(f"{fruit} not found")
    
    return add_fruit, remove_fruit

if __name__ == '__main__':
    add_fruit, remove_fruit = manage_fruit_list()
    
    add_fruit('grape')
    add_fruit('banana')
    remove_fruit('apple')
    print(fruits)