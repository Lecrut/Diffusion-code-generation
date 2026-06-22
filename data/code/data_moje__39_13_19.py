def compute_prism_volume(base_surface, vertical_dimension):
    intermediate_product = base_surface * vertical_dimension
    return intermediate_product

if __name__ == '__main__':
    sample_base = 12.5
    sample_height = 8.2
    result = compute_prism_volume(sample_base, sample_height)
    print(result)