def main():
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
    
    add_fruit('grape')
    remove_fruit('banana')
    print("Current fruits:", fruits)

if __name__ == '__main__':
    main()