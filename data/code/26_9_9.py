result = lambda x, y: x > y; print(result(10, 5))
if __name__ == '__main__':
    result = lambda x, y: x > y
    sample_output = "x=10, y=5 => True" if (lambda x, y: x > y)(10, 5) else "False"
    print(sample_output)