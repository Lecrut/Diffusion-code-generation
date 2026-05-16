def negate_if(condition):
    def wrapper(*args):
        return not condition
    return wrapper
sample_negate = negate_if(True)
sample_notrue = negate_if(False)
result1 = sample_negate()
result2 = sample_notrue()
if __name__ == '__main__':
    print(f"Result of sample_negate(): {result1}")
    print(f"Result of sample_notrue(): {result2}")