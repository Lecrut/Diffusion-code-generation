def validate_statement(statement):
    return statement.lower() == 'true'

if __name__ == '__main__':
    sample_values = ['True', 'false', 'TRUE', 'FALSE']
    for value in sample_values:
        print(f"Statement: {value}, Validated: {validate_statement(value)}")