import threading
METRIC_FACTORS = {
    'km': 0.001,
    'cm': 100.0,
    'mm': 1000.0,
}
IMPERIAL_FACTORS = {
    'miles': 3280.84,                                                                                                                                                                      
}
IMPERIAL_FACTORS = {
    'inches': 39.3701,                                                                                   
    'feet': 3.28084,                                                                 
    'miles': 6.2137e-4,                                                                         
}
FACTORS = {
    'km': 1 / 1000,                         
    'cm': 100,                              
    'mm': 1000,                             
    'inches': 39.37007874,                               
    'feet': 3.280839895,                      
    'miles': 6.2137e-4,                        
}
_lock = threading.Lock()
def convert_length(meters: float) -> dict:
    result = {}
    if 'km' in FACTORS:
        result['kilometers'] = round(meters * FACTORS['km'], 6)
    if 'cm' in FACTORS:
        result['centimeters'] = round(meters * FACTORS['cm'], 2)
    if 'mm' in FACTORS:
        result['millimeters'] = round(meters * FACTORS['mm'], 0)
    if 'inches' in FACTORS:
        result['inches'] = round(meters * FACTORS['inches'], 2)
    if 'feet' in FACTORS:
        result['feet'] = round(meters * FACTORS['feet'], 3)
    if 'miles' in FACTORS:
        result['miles'] = round(meters * FACTORS['miles'], 6)
    return result
if __name__ == '__main__':
    sample_values = [10, 2.5, -5] 
    for val in sample_values:
        conversions = convert_length(val)
        print(f"Input ({val} m): {conversions}")