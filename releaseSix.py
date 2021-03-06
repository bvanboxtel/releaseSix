
'''

For these drills you will be making functions that use all of the

skills we've covered in the units so far. This includes variables,

math operators, comparison operators, conditional statements, loops,

and functions.



'''





'''

1) Make a function that takes two parameters: a list(list), 

and a string(name).

In the function you should make a loop that runs through the list,

and check if the name is in the list. If the name is in the list,

return the name. If the name isn't in the list, return "no".



Once done making the function, make a list of five names, and 

a string variable storing another name.

Then call your function, putting in these two variables as the

parameters.

Finally, store what your function returns in another variable and

print out that variable.

'''



#WRITE CODE HERE (OUTSIDE THE COMMENTS)

def NameInList(name, list):

    if name in list

        return name

    else:

        return "nope"

    

listname = ["Sydney", "Morgan", "Kk", "Jamie", "Bella" ]

name = "Blau"



output = NameInList(name, listname)

print(output)





'''

2) Make a function that calculates the Pythagorean theorem for 

one side of a right triangle.



The Pythagorean Theorem is:



a**2 + b**2 = c**2



Here is a website with more info:

https://en.wikipedia.org/wiki/Pythagorean_theorem



You will also need the sqrt() function. Here is an example:

print(sqrt(4))

The computer would print(it looks weird but it's just 2):

(2+0j)

This can also be stored in variables like:

x = sqrt(4)



You must also copy paste the following line to the top of you code:

from cmath import sqrt



Your function should take two parameters(a and b). Then the function

should solve for c. Once solved, you should return c.



Once done making the function, make two variables for the two

sides of the triangle.

Then call your function, putting in these two variables as the

parameters.

Finally, store what your function returns in another variable and

print out that variable.

'''



#WRITE CODE HERE (OUTSIDE THE COMMENTS)



from cmath import sqrt



def pythagorean(b, a):

    c = sqrt(b**2 + a**2)

    return c



sidea = 10

sideb = 15

Hypotonuse = pythagorean(sidea, sideb)



print(Hypotonuse)