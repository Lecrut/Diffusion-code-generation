fruits = ['apple', 'banana', 'orange']

def add_fruit(fruit):
    fruits.append(fruit)

def remove_fruit(fruit):
    if fruit in fruits:
        fruits.remove(fruit)

if __name__ == '__main__':
    add_fruit('grape')
    remove_fruit('banana')
    print(fruits)