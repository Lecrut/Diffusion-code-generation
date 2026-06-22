def evaluate_or_condition(val_one, val_two):
    thresholds = {"val_one": 10, "val_two": 10}
    conditions = {
        "val_one": val_one > thresholds["val_one"],
        "val_two": val_two > thresholds["val_two"]
    }
    return conditions["val_one"] or conditions["val_two"]

if __name__ == '__main__':
    a = 15
    b = 7
    result = evaluate_or_condition(a, b)
    print(result)