import random
def select_three_unique_names(names):
    if len(names) < 3:
        return []
    selected_names = random.sample(names, 3)
    return selected_names
if __name__ == '__main__':
    name_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
    result = select_three_unique_names(name_list)
    print(result)