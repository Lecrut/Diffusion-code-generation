class FirstElementDecorator:
    @staticmethod
    def get_first_element(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, list) and len(result) > 0:
                return result[0]
            return None
        return wrapper

@FirstElementDecorator.get_first_element
def generate_numbers():
    return [5, 15, 25, 35, 45]

if __name__ == '__main__':
    print(generate_numbers())