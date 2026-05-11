def create_and_print_list():
    sample_list = []
    for i in range(10):
        if i % 2 == 0:
            sample_list.append(f"String item {i}")
        else:
            sample_list.append(i * 10)
    print("Dynamically created list:")
    for index, item in enumerate(sample_list):
        print(f"{index + 1}: {item}")
if __name__ == '__main__':
    create_and_print_list()