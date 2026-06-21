def fetch_last_element(elements):
    if not elements:
        return None
    return elements[-1]

if __name__ == '__main__':
    fruits = ["grape", "orange", "mango"]
    last_fruit = fetch_last_element(fruits)
    print(f"The last fruit in the list is: {last_fruit}")