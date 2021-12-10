# PUT YOUR NAME HERE                 <--- so we know who you are
# PUT YOUR UserID HERE               <--- so we know who you are
# F28PL Coursework 1, Python         <--- leave this line unchanged 

# Deadline is Wednesday 27 October 2021 at 15:30, local time for your campus (Edinburgh or Dubai).

# It is not your marker's role to debug basic syntax errors.
# Therefore, if your script won't compile then it might not be marked.
# In other words: if `python3 py_cw.py` won't execute, then your marker is not obliged to mark your answers. 

# To do this coursework, FORK, THEN CLONE the gitlab project.

# If you do it the other way around, then you'll have cloned *my* project (which you can't `git push` to), rather than cloned *your fork* of the project (which you can `git push` to).  
# Any questions, don't guess: ask.

# You may assume variables, procedures, and functions defined in earlier questions
# in your answers to later questions, though you should add comments in code explaining
# this if any clarification might help read your code.

# The test file test_cw.py is not exhaustive. 
# Just because your answer passes it does not mean it's correct.
# You would do well to consider where errors might be lurking and to add these to test_cw.py.   
# You are not marked directly on the quality of additional tests, however your marker may be
# able to assign marks for understanding as demonstrated in any tests you may write, 
# even if the code itself isn't quite right. 


# This coursework is live exam material so KEEP YOUR ANSWERS PRIVATE.  

# Do not delete the text from here ... 
################################################################################
# Question 1   


"""
The complex numbers are explained here (and elsewhere):
 http://www.mathsisfun.com/algebra/complex-number-multiply.html
Represent a complex integer as a pair of integers, so (4,5) represents 4+5i (or 4+5j, depending on the complex numbers
notation you use).
1a. Using def, define functions cadd and cmult representing complex integer addition and
multiplication.
For instance,
 cadd((1,0),(0,1))
should compute
 (1,1).
1b. Python has its own native implementation of complex numbers. Write translation functions
* tocomplex and 
* fromcomplex 
that map the pair (x1,y1) to the complex number x1+(y1)j and vice versa. 
You may use the python methods real and imag without comment, but not complex -- use j directly instead.
"""
# ... to here

# Check: have you read the question?  Have you read the link above to see how complex number addition and multiplication work?   


# Your answer here


#####################################
# Question 1a


def cadd(c1, c2):
    #Adding first element of both tuples and second element of both tuples and
    #then returning the result into the element
    return ((c1[0] + c2[0]),(c1[1]+c2[1]))

def cmult(c1,c2):
    #Multiplying both the tuples using the complex multiplication method
    return (((c1[0] * c2[0])+(c1[1] * c2[1])),((c1[0]*c2[1])+(c1[1] * c2[0])))


####################################
# Question 1b

def tocomplex(x1, y1):
    #Converting two numbers into one complex number
    #Multiplying 1j with the second number to convert it
    return x1 + (y1*(1j))

def fromcomplex(c):
    #Returning real part and the complex part of complex number into a tuple
    return ((int)(c.real),(int)(c.imag))


# END ANSWER TO Question 1
################################################################################


################################################################################
# Question 2


"""
2a. Using def, write iterative functions 
* seqaddi and 
* seqmulti 
that implement pointwise
addition and multiplication of integer sequences.
For instance
 seqaddi([1,2,3],[-1,2,2])
should compute
 [0,4,5]
You need not write error-handling code to handle the cases that sequences have different
lengths.
2b. Do as for 2a, but make your functions recursive (like OCaml).
Call them seqaddr and seqmultr.
2c. Do it again. This time use list comprehensions instead of iteration or recursion.
Call them seqaddlc and seqmultlc.
"""

#####################################
# Question 2a


def seqaddi(l1, l2):
    #Taking a temporary list
    l3=[]
    #Running the for loop till the length of list 1
    for i in range(0,len(l1)):
        #Appending the addition of the elements of list at same position
        l3.append(l1[i] + l2[i])
    #Returning the resulting list
    return l3

def seqmulti(l1, l2):
    #Taking a temporary list
    l3=[]
    #Running the for loop till the length of list 1
    for i in range(0,len(l1)):
        #Appending the multiplication of the elements of list at same position
        l3.append(l1[i] * l2[i])
    #Returning the resulting list
    return l3

#####################################
# Question 2b


def seqaddr(l1, l2):
    #Cheking if the length of the first list is 0
    #If it is 0 then returning empty list
    if(len(l1)==0):
        return []
    #Else returning the list with popping the first element from both lists and adding them in the list
    return [(l1.pop(0)+l2.pop(0))]+seqaddr(l1, l2)

def seqmultr(l1, l2):
    #Cheking if the length of the first list is 0
    #If it is 0 then returning empty list
    if(len(l1)==0):
        return []
    #Else returning the list with popping the first element from both lists and multiplying them in the list
    return [(l1.pop(0)*l2.pop(0))]+seqmultr(l1, l2)


#####################################
# Question 2c


def seqaddlc(l1,l2):
    #Here, we are using list comprehension
    #First, we are running the loop till the length of list and then adding both the elements of lists in list
    l3=[(l1[i]+l2[i]) for i in range(0,len(l1))]
    #Hence, Returning the list
    return l3


def seqmultlc(l1,l2):
    #Here, we are using list comprehension
    #First, we are running the loop till the length of list and then multiplying both the elements of lists in list
    l3=[(l1[i]*l2[i]) for i in range(0,len(l1))]
    #Hence, Returning the list
    return l3



# END ANSWER TO Question 2
################################################################################

################################################################################
# Question 3

"""
Write functions
* ismatrix
This should input a list of list of integers (henceforth an intmatrix) and test whether a list
of lists of integers represents a matrix (so the length of each row should be equal).
* matrixshape
This should input an intmatrix and return the size of the matrix, which is the number of rows and the number of columns 
(traditionally the number of rows is given first, but if you have it the other way around that's fine; just make sure to clearly explain your code).
* matrixadd
Matrix addition, which is simply pointwise addition.
* matrixmult
Matrix multiplication, which is not simply pointwise multiplication.

In the programs above, you do not need to write error-handling code, e.g. for the cases that 
inputs do not represent matrices or represent matrixes of the wrong shapes.
So for instance your matrixshape may assume that the argument has successfully passed the test 
ismatrix.
Your answer can use iteration, recursion, list comprehension, or anonymous functions. You
should not appeal to any libraries, e.g. for matrix processing.  Don't use zip.

You would do well to carefully comment your code, so your marker might award some marks
even for imperfect results. 
"""

def ismatrix(m):
    #Running for loop for the number of the rows
    for i in range(0,len(m)):
        #Taking the length of first row and storing it in variable
        le = len(m[i])
        #Running for loop for all the other rows to compare
        for j in range(i,len(m)):
            #If the length is not equal then returning False
            if(le!=len(m[j])):
                return False
    #If the loop completes then returning true because the number row's elements are same
    return True

def matrixshape(m):
    # Number of rows first, and number of columns second
    l = (len(m),len(m[0]))
    return l

def matrixadd(m1,m2):
    #Taking Temporary list to staore resulting matrix
    m3=[]
    #Running for loops for the rows
    for i in range(0,len(m1)):
        #taking the temporary list for the resulting rows
        temp = []
        #Running loop for the columns of the rows
        for j in range(0,len(m1[i])):
            #Appending row's value inside temporary list after adding value
            temp.append(m1[i][j] + m2[i][j])
        #Appending the rows into the matrix
        m3.append(temp)
    #Returning the resulting matrix
    return m3

def matrixmult(m1,m2):
    #Taking Temporary list to staore resulting matrix
    m3=[]
    #Running for loops for the rows
    for i in range(0,len(m1)):
        #taking the temporary list for the resulting rows
        tmp=[]
        #Running loop for the columns of the rows
        for j in range(0,len(m2[0])):
            #Taking sum as 0
            sum1 = 0
            for k in range(0,3):
                #Adding the values after multiplication
                sum1+=m1[i][k]*m2[k][j]
            #Appending the row's value
            tmp.append(sum1)
        #Appending rows into the matrinx
        m3.append(tmp)
    #Returning the resulting matrix
    return m3


# END ANSWER TO Question 3
################################################################################


###############################################################################
# Question 4


"""
Write an essay on Python data representation. Be clear, to-the-point, and concise. Convince
your marker that you understand:
* Mutable vs immutable types. Give at least two examples of each, with explanation.
* Integer vs float types.
* Assignment = vs equality == vs identity is.
* The computational effects of a call to list on an element of range type, as in
 list(range(5**5**5)).
* Slices, with examples. Including an explanation of the difference in execution between
 list(range(10**10)[10:10]) and
 list(range(10**10))[10:10]
Include short code-fragments where appropriate (as I do when lecturing) to illustrate your
observations.
"""



# END ANSWER TO Question 4
################################################################################


###############################################################################
# Question 5
"""
Write a general encoding function encdat that will input an integer, float, complex number, or
string, and return it as a string.

So
* encdat(-5) should return '-5'
* encdat(5.0) should return '5.0'
* encdat(5+5j) should return '5+5j' -- NOTE: not '(5+5j)'.
* encdat('(5))(') should return '(5))('

Do not just immediately hit the input with `str`, using it as a function that inputs an integer, float, complex number or string, and returns a string, since that guts the question. 
"""


def encdat(dat):
    #Checking if the type of argument is string or not
    if type(dat)!=str:
        #Then converting it into string
        val = str(dat)
        #If the type of argument is complex
        if type(dat)==complex:
            #Then taking the value after removing the brackets
            val = val[1:-1]
    #if it is a sting then storing it in the value
    else:
        val = dat
    #Returning the result
    return val

# END ANSWER TO Question 5
################################################################################


###############################################################################
# Question 6


"""
An encoding f of numbers in lists is as follows:
* f(0) = [] (0 maps to the empty list)
* f(n+1) = [f(n),[f(n)]] (n+1 maps to the list that contains f(n) and singleton f(n))
Implement encode and decode functions in Python, that map correctly between nonnegative
integers and this representation. Call them fenc and fdec.

This is an implementation of one possible encoding of the natural numbers in sets:
   https://en.wikipedia.org/wiki/Set-theoretic_definition_of_natural_numbers
"""


def fenc(i):
    #If i is equal to 0 then returning the empty list
    if i==0:
        return []
    #Else it calls the same function for i-1 times and after execution returns the same result
    return [fenc(i-1),[fenc(i-1)]]

def fdec(l):
    #Number for calculating
    num=0
    #Running while loop for the lists till its not empty
    while(l!=[]):
        #Incrementing the number for every list
        num+=1
        #Updating the list with the first value in it
        l = l[0]
    #Returning the number
    return num


# END ANSWER TO Question 6
################################################################################


###############################################################################
# Question 7


"""
Implement a generator cycleoflife such that if we assign
 x = cycleoflife()
then repeated calls to
 next(x)
return the values
 eat
 sleep
 code
 eat
 sleep
 code
 ...
in an endless cycle. If you can't manage an endless cycle, do a program that runs for 1000
cycles then stops.
Note that this question is not asking you to program an endless loop that prints these values.
In effect, I am asking you to implement what is called a stream (infinite list)
 x = [eat, sleep, code, eat, sleep, code, ...].
This does not mean the whole infinite datastructure is in memory at any time (which is 
impossible for a machine with finite memory), but for any finite but unbounded number of calls 
to next your generator behaves as if it were the infinite datastructure illustrated above.
"""


def cycleoflife():
    #Taking list for storing the words to append
    lst = ['eat','sleep','code']
    #Taking temporary list for appending the lisy
    tmp = []
    #Running while loop for infinite times
    while(True):
        #Running for loop for the length of the list
        for i in range(len(lst)):
            #Appending the list
            tmp.append(lst[i])
            #Generating the result
            yield(lst[i])




# END ANSWER TO Question 7
################################################################################


#################################################################################
# Question 8

"""
Call a *datum* something that is either an integer, or a list of data (datums).

Write a flatten function gendat that converts a datum to a list of integers.

So
- gendat(5) should return [5]
- gendat([])should return []
- gendat([5,[5,[]],[],[5]]) should return [5,5,5]

Do not use str.  You may find it useful to consider isinstance or the following code fragment
   type(5) == type([]) 
"""


def gendat(datum):
    #Checking if the type of argument is list of not
    if type(datum) is list:
        #If it is a list then calling the same function inside the loop
        return [x for lists in datum for x in gendat(lists)]
    #If the type is not list then returning the result into the list
    else:
        return [datum]


# END ANSWER TO Question 8
################################################################################


##########################################################
# Question 9

"""
Implement the Sieve of Eratosthenes
 https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
as a Python generator eratosthenes such that if we assign
 x = eratosthenes()
then repeated calls to
 next(x)
return the primes, starting from 2.
"""

def eratosthenes():
    #Taking List for infinite inputs
    n=[False]
    #Running for loop within that list
    for i in n:
        #Appending the value in the list
        n.append(False)
        #Taking the valriable for storing length of the list
        lnt = len(n)
        t=0
        #If the length is 2 or 3 then taking the length
        if lnt==2 or lnt==3:
            yield lnt
        #If length is not same then 
        else:
            #Running for loop from 2 till length-1
            for d in range(2,lnt-1):
                #If the remainder of the modulus is 0 then assigning 1 to temp because it is not prime number
                if lnt%d==0:
                    t=1
            #If the temp is 0 then it is a prime number
            if t==0:
                yield lnt




# For reference, here is an implementation of the sieve of Eratosthenes, 
# whose argument acts as a bound on the returned generator (40000, by default). 
# Your answer should take no argument, and should return an unbounded generator.
def eratosthenes(z=40000):
    # create an array of true values the size of z
    A = [True] * z
    # iterate over each value to z squared
    for x in range(2, int(z ** 0.5)):
        # if A[x] has a true value
        if A[x]:
            # iterate over a range starting from x*2 ending at z in jumps of x
            for z in range(x * 2, z, x):
                # set anything in the range to false
                A[z] = False
    # iterate over the array
    for y in range(2, len(A)):
        # if a value is true that index is a prime number
        if A[y]:
            # yield the current iterator location as it is a prime
            yield y




# END ANSWER TO Question 9
################################################################################


################################################################################
# Question 10

"""
Following on from Question 3, invertible matrices are explained here:
   https://en.wikipedia.org/wiki/Invertible_matrix
   https://en.wikipedia.org/wiki/Minor_(linear_algebra)#Inverse_of_a_matrix

Write and test an algorithm to calculate the inverse of an n x n matrix (i.e. a square matrix) using Cramer's rule, for n>=1.

* Your answer should include helper functions (and tests for them) to calculate the
* *determinant*,
* *minors*,
* *cofactors*, and
* *adjoint* of a matrix, all of which are described here:
   https://en.wikipedia.org/wiki/Minor_(linear_algebra)
   https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html
* Your code will be marked on clarity as well as correctness.  Code that is "correct" but unreadable, is bad code and therefore may get bad marks.

Writing, documenting, and testing helper functions is generally good practice, and you will likely find other helper functions are required, such as for matrix transpose, computing a sub-matrix, multiplying a matrix by a scalar, and perhaps others.  

Whatever you do, just make sure you explain what you're doing and why. 
"""

def matrixtranspose(m):
    mat=[]
    for i in range(0,len(m)):
        temp=[]
        for j in range(0,len(m[i])):
            temp.append(m[j][i])
        mat.append(temp)
    return mat   

def matrixsub(m, p, q):
    sub=[]
    for k in range(len(m)):
        tmp=[]
        for j in range(len(m[k])):
            if k!=p and j!=q:
                tmp.append(m[k][j])
        if tmp:
            sub.append(tmp)
    return sub

def matrixminors(m):
    min=[]
    for i in range(len(m)):
        tmp=[]
        for k in range(len(m[i])):
            sub = matrixsub(m,i,k)
            tmp.append((sub[0][0]*sub[1][1])-(sub[1][0]*sub[0][1]))
        min.append(tmp)
    return min

def matrixdeterminant(m):
    min = matrixminors(m)
    tmp=[]
    sum=0
    for i in range(len(min[0])):
        tmp.append(((-1)**(0+i))*m[0][i])
        sum = sum + (tmp[i]*min[0][i])
    return sum

def matrixcofactors(m):
    min=matrixminors(m)
    c = []
    for i in range(len(min)):
        tmp = []
        for k in range(len(min[i])):
            tmp.append(((-1)**(i+k))*min[i][k])
        c.append(tmp)
    return c

def matrixadjoint(m):
    return matrixtranspose(matrixcofactors(m))

def matrixscale(s, m):
    arr=[]
    for i in range(len(m)):
        arr.append([s[i][0]*m[i][i]])
    return arr

def matrixinverse(m):
    aj = matrixadjoint(m)
    det = matrixdeterminant(m)
    inverse = []
    for i in range(len(aj)):
        tmp=[]
        for j in range(len(aj[i])):
            tmp.append(aj[i][j]/det)
        inverse.append(tmp)
    return inverse



# END ANSWER TO Question 10
################################################################################


###############################################################################
# Question 11

"""
Write a brief but comprehensive essay that:
1. Surveys the modern uses and applications of Python.
2. Speculates on what it is about Python that has led to its popularity.
3. Speculates on the evolution of Python into the future.  

Your essay should not be long.  

For full marks your answer should demonstrate both factual and technical understanding of the programming languages landscape in general, and of Python's role --- technically, economically, and socially --- within it.
"""


"""
Here's a very brief example answer to Q11 above where "Python" is replaced by "Eggs".  Enjoy:

A chicken is cheap to keep, can produce an egg a day, and eggs come prepackaged and naturally resist spoilage.  For instance, eggs come out of a chicken with a natural antibacterial coating on their shells so that they can be stored at room temperature, which keeps transport costs low --- in the US eggs are washed, which stops them smelling of chickens' bottoms but removes this coating, which is why US eggs require refrigeration and UK eggs don't. 
[note now this combines *factual* and *technical* elements; an awareness of the egg as a thing, but also of supply chain economics, food safety, and a nice factoid which really proves I went beyond the first page of Google results -mjg] 

Eggs are nutritious, tasty, and filling.  They are easy to cook and are culturally well-established in the UK.  A proper superfood, in fact.  

Eggs do have dangers: when improperly handled they can carry salmonella.  More information at [hyperlink].  Eggs can crack, and then spoil quickly.  Occasionally eggs go invisibly bad, or the embryo incubates prematurely (nowadays, sophisticated scanning machines eliminate these from the food chain). 

Eggs also have applications in vaccine development, and unfortunately also in biological warfare as incubators for germs, and [more stuff here -mjg].

For the future, [stuff about vegans, changes in food preferences, vat-grown protein, environmental costs of keeping chickens, etc etc].

[I could keep this up for pages, I won't: we've gone beyond the shell of an answer, we've cracked it, and if we allow our enthusiasm to egg us on then it would over-egg the pudding and we'd get egg on our faces for writing a not-eggsactly-concise answer:  we stuffed enough eggs in this basket and should stop, before the reader finds it eggscrutiating.   
Now your turn please, with "Python" instead of "Egg".  Make me proud.  -mjg]
""" 

'''
Nowadays, Python is one of the most popular languages because of its ease to use, simple syntax, and it's too versatility. 
Many third-party libraries are available in this language which makes the developer's work easier in many ways. Due to these 
libraries, Python is used in creating websites with the best user experience and usability. Many software is built using python 
like computer applications or mobile applications including game development. GUI libraries like Tkinter are used to create 
applications that take user experience to another level. Due to some advanced libraries, Python helps data scientists in 
analyzing data using graphs and charts. Because of this automation can be done using Python so that one can keep the track 
of many things. For example, during COVID-19, many developers created software using python to keep track of cases all over 
the world. The user can have proper visualization of the data collected using python during the pandemic or for many other tasks.

The main reason behind python's popularity is the third-party libraries which makes it easier for beginners to have confidence 
in the vast world of programming and they can create their software easily according to their requirements. Many non-programmers 
also started using python because of its uses and easiness. Because of the third-party applications, python kept updating on its 
own and with the use of developers in the world. 

If we see the use of python nowadays, we can clearly say that python can be the language of the future because of the reasons 
given above. I hope python will develop more artificial intelligence and machine learning tools so that more developers can use them.
The main reason python will grow in the future is because it is open-source which means it is free to use for everyone all over the world.
'''
# END ANSWER TO Question 11 
###############################################################################

###############################################################################
# Question 12

"""
Python has infinite precision integer arithmetic.

Write your own infinite precision "sum", "product", and "to the power of" functions, that represent numbers as lists of digits between 0 and 9 with least significant digit first. 
Thus: 0 is represented as the empty list [], and 10 is represented as [0,1]. 
You may assume that numbers are non-negative (no need for negative numbers, or for subtraction).
Do NOT gut the question by mapping to python's native integers, performing the arithmetic there, and mapping back!
You may use earlier functions in the definitions of later ones. 

Add your own tests to the `test_cw.py` file.
"""

# map an integer n to its representation as a string of digits.
# no need to error-check for the case that n is negative
# e.g. iint(12) == [2,1]
def iint(n):
    #Taking temporary list for storing
    tmp = []
    #If the number is greater than 0
    if n>0:
        #Running while loop till n is not 0
        while n!=0:
            #Appending the last value of integer in the list
            tmp.append(n%10)
            #Updating the number n
            n = (int)(n/10)
    #Returning the list
    #If it is 0 then returning the empty list
    return tmp


# map the string-of-digit representation back to integers
# e.g. pint(iint(12)) == 12 
def pint(I):
    #Taking Number as 0
    n=0
    #For running for loop from length of list will the last value
    for i in range(len(I),0,-1):
        #Multiplying the number and adding it to n
        n = n*10 + I[i-1]
    #Returning the Number
    return n

# add two infinite integers
def iadd(I,J):
    return I+J

# multiply two infinite integers
def imult(I,J):
    return I*J

# raise I to the power of J
def ipow(I,J):
    pass 
