import sys
def build_list_from_samples():
    items = ["apple", "banana", "cherry", "date"]
    final_list = []
    for item in items:
        if item:
            final_list.append(item)
    return final_list
if __name__ == '__main__':
    result = build_list_from_samples()
    print(result)