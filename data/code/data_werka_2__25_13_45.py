def is_effectively_zero(values):
    tolerance = 1e-10
    
    def is_close_to_zero(value):
        if isinstance(value, (int, float)):
            return abs(value) < tolerance
        elif isinstance(value, complex):
            return abs(value.real) < tolerance and abs(value.imag) < tolerance
        else:
            raise ValueError(f"Unsupported type: {type(value)}")
    
    return [is_close_to_zero(value) for value in values]

if __name__ == '__main__':
    sample_values = [0, 1e-12, -1e-13, 0.0, 1+0j, 0+0j, 1e-14 + 1e-15j]
    result = is_effectively_zero(sample_values)
    print(result)