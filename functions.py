def count_glass(list_1):
    count = 0
    glassnie = 'ауоыиэяюёе'
    for i in list_1:
        if i in glassnie:
            count += 1
    return count