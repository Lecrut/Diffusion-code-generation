conversion_factor = {'nm_to_m': 1e-09}

def nanometers_to_meters(nanometers):
    return nanometers * conversion_factor['nm_to_m']
if __name__ == '__main__':
    sample_nm = 500000000
    meters = nanometers_to_meters(sample_nm)
    print(f'{sample_nm} nanometers is equal to {meters} meters')