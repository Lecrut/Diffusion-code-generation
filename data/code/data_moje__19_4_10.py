import random

def select_random_row(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    total_rows = len(data)
    target_index = random.randint(0, total_rows - 1)
    return data[target_index]

if __name__ == '__main__':
    dataset = [
        ["alpha", 100, "red"],
        ["beta", 200, "blue"],
        ["gamma", 300, "green"],
        ["delta", 400, "yellow"],
        ["epsilon", 500, "purple"]
    ]
    chosen_row = select_random_row(dataset)
    print(chosen_row)