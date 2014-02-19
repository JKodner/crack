import random
def sep(s, n):
    print s * n
code = []
count = 1
tries = 0
print 
sep("=", 50)
length = " "
while type(length) != int:
    try:
        length = int(raw_input("How Many Numbers in The Code Do You Want?"))
        if not length >= 3:
            length = " "
            print "Code Length Must be Greater Than Or Equal to 3."
    except ValueError:
        None
sep("=", 50)
print
while len(code) < length:
    i = random.choice(range(0, 10))
    if i not in code:
        code.append(i)
code.sort()
print
sep("-", 50)
print "The Numbers In Your Code Are: " + str(code)
print "Scrambling the Code..."
sep("-", 50)
print
print_c = code[:]
for i in range(5):
    random.shuffle(code)
print print_c
while count - 1 != len(code):
    if count == 1:
        print_count = str(count) + "st"
    elif count == 2:
        print_count = str(count) + "nd"
    elif count == 3:
        print_count = str(count) + "rd"
    else:
        print_count = str(count) + "th"
    ask = raw_input("Guess the %s Number In The Code: " % print_count)
    position = count - 1
    try:
        ask = int(ask)
        if ask == code[position]:
            sep("-", 50)
            print "Correct!"
            sep("-", 50)
            count += 1
        else:
            sep("-", 50)
            print "Wrong."
            sep("-", 50)
            count = 1
    except ValueError:
        sep("-", 50)
        print "Wrong."
        sep("-", 50)
        count = 1
    tries += 1
print
sep("=", 50)
print "You Cracked the Code!"
print "The Code Was: " + str(code)
print "You Took %d Turns To Crack The Code!" % tries
count += 1
sep("=", 50)
print