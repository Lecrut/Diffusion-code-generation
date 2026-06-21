def manage_fruit_list():
    fruits = ['apple', 'banana', 'orange']
    
    def add_fruit(fruit):
        if fruit not in fruits:
            fruits.append(fruit)
            return True
        return False
    
    def remove_fruit(fruit):
        if fruit in fruits:
            fruits.remove(fruit)
            return True
        return False
    
    return fruits, add_fruit, remove_fruit

if __name__ == '__main__':
    fruits, add_fruit, remove_fruit = manage_fruit_list()
    
    print("Initial fruits:", fruits)
    
    if add_fruit('grape'):
        print("Added grape:", fruits)
    else:
        print("Grape already exists.")
    
    if remove_fruit('banana'):
        print("Removed banana:", fruits)
    else:
        print("Banana not found.")