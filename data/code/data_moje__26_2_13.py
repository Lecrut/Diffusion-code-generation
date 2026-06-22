def is_adult(citizen):
    return 'age' in citizen and citizen['age'] >= 18

if __name__ == '__main__':
    sample_adult = {'name': 'Alice', 'age': 25}
    sample_minor = {'name': 'Bob', 'age': 16}
    sample_no_age = {'name': 'Charlie'}
    print(is_adult(sample_adult))
    print(is_adult(sample_minor))
    print(is_adult(sample_no_age))