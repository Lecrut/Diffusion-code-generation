if __name__ == '__main__':
    data = [("Alice", 35), ("Bob", 28), ("Charlie", 31), ("David", 40), ("Eve", 29)]
    filtered_data = [(name, age) for name, age in data if age > 30]
    print(filtered_data)