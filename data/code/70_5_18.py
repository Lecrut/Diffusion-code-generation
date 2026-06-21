class EndElementValidator:
    _status_codes = {
        200: "OK",
        400: "Bad Request",
        404: "Not Found",
        500: "Internal Server Error"
    }

    def __init__(self, items):
        self.items = items

    def get_end_elements(self):
        if len(self.items) < 2:
            raise ValueError("List must contain at least two elements")
        return self.items[0], self.items[-1]

if __name__ == '__main__':
    validator = EndElementValidator([100, 200, 300, 400])
    first, last = validator.get_end_elements()
    print(first, last)