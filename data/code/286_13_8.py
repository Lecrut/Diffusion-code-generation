conversion_factor = {
    'mm_to_in': 0.0393701,
}

def mm_to_inches(mm):
    return mm * conversion_factor['mm_to_in']

if __name__ == '__main__':
    print(mm_to_inches(25))
    print(mm_to_inches(100))