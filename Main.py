l = ['magical','unicorns']

sum_int = 0
all_str = ""
for thing in l:
    if isinstance(thing, float) or isinstance(thing, int):
        sum_int += thing

    elif isinstance(thing, str):
        all_str += thing + ' '

if sum_int and all_str:
    print "The list you entered is of mixed type"
elif sum_int:
    print "The list you entered is of integer type"
elif all_str:
    print "The list you entered is of String type"

if all_str:
    print "String:", all_str
if sum_int:
    print "Sum:", sum_int