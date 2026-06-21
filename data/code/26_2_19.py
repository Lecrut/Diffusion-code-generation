def is_adult(citizen):
    if 'age' not in citizen:
        return False
    if not isinstance(citizen['age'], (int, float)):
        return False
    return citizen['age'] >= 18

if __name__ == '__main__':
    sample_citizen = {'name': 'Alice', 'age': 20}
    print(is_adult(sample_citizen))
    sample_minor = {'name': 'Bob', 'age': 17}
    print(is_adult(sample_minor))
    sample_no_age = {'name': 'Charlie'}
    print(is_adult(sample_no_age))