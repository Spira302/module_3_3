def print_params(a=1, b='string', c=True):
    print(a, b, c)


values_list = [1, 'drinks', False]
values_dict = {'a':52, 'b':'Alblack', 'c':True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [1, 'kishlak']
print_params(*values_list_2, 42)
