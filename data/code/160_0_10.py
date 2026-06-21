fruits = ['apple', 'banana', 'orange']

def add_fruit(fruit):
    if fruit not in fruits:
        fruits.append(fruit)
    else:
        print(f'{fruit} already exists in the list.')

def remove_fruit(fruit):
    if fruit in fruits:
        fruits.remove(fruit)
    else:
        print(f'{fruit} does not exist in the list.')
if __name__ == '__main__':
    add_fruit('grape')
    print(fruits)
    remove_fruit('banana')
    print(fruits)