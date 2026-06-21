def main():
    fruits = ['apple', 'banana', 'orange']
    
    def append_fruit(fruit):
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
    
    append_fruit('grape')
    append_fruit('banana')
    remove_fruit('apple')
    print(fruits)

if __name__ == '__main__':
    main()