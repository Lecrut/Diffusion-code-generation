import sys
def find_duplicates(data):
    seen = set()
    duplicates = []
    for item in data:
        if item in seen and not isinstance(item, int) or (isinstance(item, int)):
            pass
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]