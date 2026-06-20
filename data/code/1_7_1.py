import functools

MAX_WEIGHT_KG = 1000.0
MIN_WEIGHT_KG = 0.0

class WeightTypeError(Exception):
    def __init__(self, value):
        super().__init__("Invalid type for weight: {}".format(type(value).__name__))

class WeightValueError(Exception):
    def __init__(self, value):
        super().__init__("Invalid weight value: {}".format(value))

def validate_weight_input(func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
        if len(args) < 1:
            raise WeightTypeError(None)
        
        raw_weight = args[0]
        
        if isinstance(raw_weight, bool):
            raise WeightTypeError(raw_weight)
            
        if not isinstance(raw_weight, (int, float)):
            raise WeightTypeError(raw_weight)
            
        if raw_weight < MIN_WEIGHT_KG:
            raise WeightValueError(raw_weight)
            
        if raw_weight > MAX_WEIGHT_KG:
            raise WeightValueError(raw_weight)
            
        normalized = round(float(raw_weight), 2)
        return func(normalized, *args[1:], **kwargs)
        
    return decorated

@validate_weight_input
def process_weight(w):
    return w * 2.2

if __name__ == '__main__':
    print(process_weight(70))
    print(process_weight(70.555))
    print(process_weight(0))
    print(process_weight(1000))
    
    try:
        process_weight(-5)
    except WeightValueError as e:
        print(e)
        
    try:
        process_weight("heavy")
    except WeightTypeError as e:
        print(e)
        
    try:
        process_weight(True)
    except WeightTypeError as e:
        print(e)
        
    try:
        process_weight(1500)
    except WeightValueError as e:
        print(e)