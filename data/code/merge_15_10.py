def main():
    item_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    print("--- Fruit List ---")
    for index, item in enumerate(item_list):
        print(f"{index + 1}. {item}")
if __name__ == '__main__':
    main()