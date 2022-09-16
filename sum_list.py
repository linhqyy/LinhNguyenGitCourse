def sum_list(lst):
    s = 0
    for i in range(len(lst)):
        try:
            s += float(i)
        except ValueError:
            pass 
    return s