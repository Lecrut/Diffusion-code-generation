VALID_TRUE = "true"
VALID_FALSE = "false"

def validate_statement(statement):
    if statement.strip().lower() == VALID_TRUE:
        return True
    elif statement.strip().lower() == VALID_FALSE:
        return False
    else:
        raise ValueError(f"Invalid value encountered: '{statement}'")

if __name__ == '__main__':
    sample_values = ["true", "false", "true", "true", "false"]
    true_count = 0
    false_count = 0

    for value in sample_values:
        try:
            if validate_statement(value):
                true_count += 1
            else:
                false_count += 1
        except ValueError as e:
            print(e)

    print(f"True count: {true_count}")
    print(f"False count: {false_count}")