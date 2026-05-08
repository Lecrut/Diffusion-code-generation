def count_true_false(data):
    true_count = 0
    false_count = 0
    for item in data:
        if item == "True":
            true_count += 1
        elif item == "False":
            false_count += 1
    return true_count, false_count
if __name__ == '__main__':
    sample_data = ["True", "False", "True", "False", "True", "True", "False"]
    true_count, false_count = count_true_false(sample_data)
    print(f"True count: {true_count}")
    print(f"False count: {false_count}")