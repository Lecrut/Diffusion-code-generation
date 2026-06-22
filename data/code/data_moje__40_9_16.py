MULTI_FACE_AREA_COEFFICIENT = 2

def compute_surface_area(length, width, height):
    face_area_lw = length * width
    face_area_wh = width * height
    face_area_hl = height * length
    total_face_sum = face_area_lw + face_area_wh + face_area_hl
    return MULTI_FACE_AREA_COEFFICIENT * total_face_sum

if __name__ == '__main__':
    dim_length = 1.5
    dim_width = 2.5
    dim_height = 3.5
    result = compute_surface_area(dim_length, dim_width, dim_height)
    print(result)