COMPARE_LABELS = {
    "first": "a",
    "second": "b",
    "third": "c"
}

def compare_three_numbers(a, b, c):
    current_max = a
    label_map = {"current": "a"}
    
    if b > current_max:
        current_max = b
        label_map["current"] = "b"
    
    if c > current_max:
        current_max = c
        label_map["current"] = "c"
    
    origin_label = COMPARE_LABELS.get(label_map["current"], "unknown")
    return current_max

if __name__ == '__main__':
    val_1 = 150
    val_2 = 88
    val_3 = 150.0001
    largest_value = compare_three_numbers(val_1, val_2, val_3)
    print(largest_value)