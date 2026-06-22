def add_floats(a: float, b: float) -> float:
    return a + b

if __name__ == '__main__':
    sample_values = {
        'pi': 3.141592653589793,
        'e': 2.718281828459045
    }
    result = add_floats(sample_values['pi'], sample_values['e'])
    print(result)