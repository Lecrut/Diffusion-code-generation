import multiprocessing
import os

def decimal_to_binary_single(value):
    if isinstance(value, int) and value >= 0:
        return format(value, 'b')
    elif isinstance(value, float):
        int_part, frac_part = divmod(value, 1)
        int_bin = format(int(int_part), 'b')
        frac_bin = ''
        if frac_part > 0:
            remainder = frac_part
            for _ in range(52):
                remainder *= 2
                bit = int(remainder)
                frac_bin += str(bit)
                remainder -= bit
                if remainder == 0:
                    break
        if frac_bin:
            return int_bin + '.' + frac_bin
        else:
            return int_bin
    else:
        return None

def decimal_to_binary_concurrent(decimal_list, max_workers=None):
    if max_workers is None:
        max_workers = min(multiprocessing.cpu_count(), len(decimal_list))
    with multiprocessing.Pool(processes=max_workers) as pool:
        results = pool.map(decimal_to_binary_single, decimal_list)
    return results

if __name__ == '__main__':
    sample_decimals = [10, 255, 1024, 0, -5, 3.14, 1000000]
    binary_results = decimal_to_binary_concurrent(sample_decimals)
    print(binary_results)