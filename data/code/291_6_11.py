conversion_table = {
    'nm': 1,
    'um': 1000
}

def compare_measures(nanometers, micrometers):
    nm_value = nanometers * conversion_table['nm']
    um_value = micrometers * conversion_table['um']
    if nm_value < um_value:
        return f"{nanometers} nm"
    else:
        return f"{micrometers} um"

if __name__ == '__main__':
    print(compare_measures(500, 2))