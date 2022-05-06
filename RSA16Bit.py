# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 03:19:15 2020

@author: Sanjeev Kumar Paul
"""
"""
Since I worked on i3 powered Laptop , Execution time was beginning to move
towards 40-45 minute range.Hence,I chose an Upper and Lower bound in random
function for finding a number.
I worked with Lists as I found it the most convenient way to store data
as compared to Dictionary
My Public value N is 24 bit in length & prime values are 12 bit each.

"""

from random import randint
candidate_p=randint(2048,4096)
candidate_q=randint(2048,4096)
print('Initial Number P & Q ',candidate_p,candidate_q)


def primegenerator(final_candidatep,final_candidateq):
    # Any Number Divisible by 2 is not odd hence picked this to find prime
    looping_value = 2
    
    # Initiate Loop while staying in the range 
    while looping_value in range(2,4896):
            # If both Initial values are odd, do Nothing
            if(final_candidatep % looping_value and
               final_candidateq % looping_value) != 0:
                
                pass
           
            # If that specific number is divisible by any number in range
            # Print that number and find a new candidate
            # Re-Initiate the loop
           
            if (final_candidatep % looping_value or
                final_candidatep == looping_value) == 0:
               
                final_candidatep = randint(2048,4896)
                print('Not Prime! Divisible by',looping_value)
                print('Changing P!....... Found New Number',final_candidatep)
                looping_value = 2
            if(final_candidateq % looping_value or
               final_candidateq == looping_value) == 0:
               
                final_candidateq = randint(2048,4096)
                print('Not Prime! Divisible by',looping_value)
                print('Changing Q! .......Found New Number',final_candidateq)
                looping_value = 2
                
                
            # When Candidate value is same as Loop Value, it satisifies
            # Condition for prime    
            
            if (looping_value == final_candidatep):
              print('found One number P',final_candidatep)
            if (looping_value == final_candidateq):
                print('found One Number Q',final_candidateq)
            looping_value = looping_value + 1    
    
    print('prime number found',final_candidatep,final_candidateq)
    
# Generating Public Key 'e' 
    
def publickey_eGenerator(candidatepublickey):
    # Any Number Divisible by 2 is not odd hence picked this to find prime
    looping_value = 2
    
    # Initiate Loop while staying in the range 
    while looping_value in range(2,phi_n):
            # If Initial value is odd, do Nothing
            if(candidatepublickey % looping_value ) != 0:
                
                pass
           
            # If that specific number is divisible by any number in range
            # Print that number and find a new candidate
            # Re-Initiate the loop
           
            if (candidatepublickey % looping_value or
                candidatepublickey == looping_value) == 0:
               
                candidatepublickey = randint(1,phi_n)
                print('Not Prime! Divisible by',looping_value)
                print('Changing P!....... Found New Number',candidatepublickey)
                looping_value = 2
            
                
                
            # When Candidate value is same as Loop Value, it satisifies
            # Condition for prime    
            
            if (looping_value == candidatepublickey):
              print('found One number P',candidatepublickey)
           
            looping_value = looping_value + 1
    return candidatepublickey
    
    print('prime number found',candidatepublickey)
    

# Function to calculate Highest Common Factor between public key and phi_n


def gcd(dividingvalue,number):
    
    # For storing quotient values, declare a list
    quotient= []
    
    # As long as the remainder is not zero, Keep the loop going
    while True:
        
        if(number % dividingvalue != 0):
            # Remainder of modulus operation stored in temporary variable
            next_term = number % dividingvalue
            
            # Increment List
            quotient.append( number // dividingvalue)
            
            # Previous divisor is our dividend in next iteration
            number = dividingvalue
            
            # Next value is our divisor in next iteration
            dividingvalue = next_term
            
        
        elif(number % dividingvalue == 0):
                # Last Divisor is our Highest Common Factor    
                gcd = dividingvalue
                print('gcd is',gcd, 'quotients were:', quotient)
                
                break
            
# Function to calculate Multiplicative Inverse
            
def modinverse(dividingvalue,number):
    
    # Declare Initial values in this process
    start1 = 0
    start2 = 1
    # To bring back the number in positive domain
    originalModValue=number
    while True:
        if(number % dividingvalue != 0):
            # Temporary variable holding remainder
            y=number % dividingvalue
            # Quotient used for find multiplicative inverse
            quotient=number // dividingvalue
            # New dividend for next iteration
            number = dividingvalue
            # New divisor for next iteration
            dividingvalue = y
            nextval =start1 - (quotient) * start2   
            start1 = start2
            start2 = nextval
            
        elif(number %dividingvalue == 0):
                # If value is negative bring to positive domain
                if(nextval < 0):
                    return nextval + originalModValue
                elif(nextval >= 0):
                    
                    return nextval
                break
 
# Function to break a number in power of 2s
        
def power_find(exponentvalue): 
   # https://stackoverflow.com/questions/30226094/how-do-i-decompose-a-number-into-powers-of-2
    
   # Declare list for storing values
    resulting_sequence = []
   # Convert the number into binary digits
    binaryvalue = bin(exponentvalue)[:1:-1]
    # Initiate Loop till we parse entire number sequence
    for x in range(len(binaryvalue)):
        
    # If the number situated is '1' , append index value to list
        if int(binaryvalue[x]):
            resulting_sequence.append(2**x)
    return resulting_sequence

# Performing Square and Multiply by picking single value of the list at time

def smalgorithmforencryption(oneitem): 
    result = 1
    for item in receivedsquareandmul: # Iterate Public Key Decomposed in power of 2s 
        result = result * oneitem ** item
        
    return result   

def smalgorithmfordecryption(seconditem): 
    startvalue = 1
    # Iterate private key decomposed in power of 2s
    for item in smdecryption: 
        startvalue = startvalue * seconditem ** item
        
    return startvalue


#Dividing the text into 3byte chunks

def conversionoftext(x):
    
    
#https://pythonexamples.org/python-split-string-into-specific-length-chunks/
    chunks = [x[i:i+byteseparationvalue]
              for i in range(0, len(x), byteseparationvalue)] 
    
    return chunks


def conversiontoint(x,y):
    
    # Converting 3 byte chunks into Hex value
    for character in x:
# https://stackoverflow.com/questions/38909543/python3-how-to-convert-a-string-to-hex
        hexequivalent.append(character.encode('utf-8').hex()) 
    
    for character in y:
        hexequivalentsigned.append(character.encode('utf-8').hex())
    
    # Converting Hex value to integers for plain text
    for character in hexequivalent:
        intequivalent.append(int(character,16))
    print('conversion steps of hex text:',hexequivalent,'--->',intequivalent)
    for character in hexequivalentsigned:
        intequivalentsigned.append(int(character,16))
    print('conversion steps of hex signed text:',
          hexequivalentsigned,'---->',intequivalentsigned)


# Function for Encryption and Decryption

         
def RSAfunc(N,e,d,intequivalent,myN):
    
    # Iterate through Plain text Chunks
    
    for iterating_everymessage in intequivalent:
        # This is what next step is accomplishing C= i**public Key  % N
        C = smalgorithmforencryption(iterating_everymessage) % N 
        # Adding values to the Encrypted text
        Encry.append(C) 
        iterating_everymessage = iterating_everymessage + 1
        
    
    print('Sending This Text to my Partner:',Encry)
    


    for through_retrievedmessage in received_message:
        
        # This is what next step is accomplishing D= y**private key  % N
        D = smalgorithmfordecryption(through_retrievedmessage) % myN
        # Incrementing Decrypted text
        Decry.append(D)
        print('Plaintext retrieved for :', through_retrievedmessage)
        through_retrievedmessage = through_retrievedmessage + 1
    
    print('Is this your plaintext?:',Decry)

# Getting Plaintext Deciphered
def backtooriginal(decryptedtext):
    
    # Converting Deciphered text back to hex
    for val in decryptedtext:
        damnit.append(hex(val))
    # Converting Hex back to text
    for x in damnit:
       # Slicing the first '0x' and decoding with utf-8 Standard 
       plaintextdecrypted.append(bytes.fromhex(x[2:]).decode('utf-8'))
      
        
# Creating Signature    
def Signedfunc(N,d,intequivalentsigned):
    for signature_pieces in intequivalentsigned:
        C = smalgorithmfordecryption(signature_pieces) % N
        signedencrypt.append(C)
    
    print('RSA Signature is:',signedencrypt)
    
# Verify Signature
def verification(recN,rece):
    for partner_signature in received_signature:
        C = smalgorithmforencryption(partner_signature) % recN 
        received_original_signature.append(C)
        
    
    # Converting Received signature back to hex
    for val in received_original_signature:
        fororiginal.append(hex(val))
    
    # Converting Hex back to text
    for hex_chunks in fororiginal:
        # https://stackoverflow.com/questions/51369750/python-valueerror-non-hexadecimal-number-found-in-fromhex-arg-at-position-1
       fororiginalplaintextreceived.append(bytes.fromhex(hex_chunks[2:]).decode('utf-8'))
    
    if(original_Signature ==  ''.join(fororiginalplaintextreceived) ):
        print('Verified Signature : RSA Encryption Successful : Well Done')
        


# Public N,e ,Signature of Sanjeev Kumar Paul

primeselected1 = 2857
primeselected2 = 3583
publickey_N = primeselected1 * primeselected2
phi_n = (primeselected1-1) * (primeselected2-1)

# Way to generate public key
candidate_e= randint(1,phi_n)
final_candidatee=publickey_eGenerator(candidate_e)

#But I chose a smaller number for faster Encryption
publickey_e = 571
byteseparationvalue = 3


Encry = []
Decry = []
Encryptionstring = []
SignedText = []
hexequivalent = []
intequivalent = []
hexequivalentsigned = []
intequivalentsigned = []
signedencrypt = []
inttohex = []
plaintextdecrypted = []
damnit = []

print('public key is:', final_candidatee)

# Public N,e, signature of Partner

received_signature = [633996786,472049645]
received_original_signature = []
received_publicN = 1411164367
received_publickey = 829
receivedsquareandmul = power_find(received_publickey)
received_message = [3118436,5380268,3985642,8360984,6792294,
                   8479955,520114,154964,3137650,1927270,921905]
received_Encry =[]
fororiginal=[]
fororiginalplaintextreceived=[]
original_Signature='farzad'

# Calling Functions and generating values

privatekey_d = modinverse(publickey_e,phi_n)
squareandmul = power_find(publickey_e)
smdecryption = power_find(privatekey_d)
print('Prime Numbers Found Using Random Function are:'
      ,primeselected1,primeselected2)
print('My Public key which is prime:',publickey_e)

print('N to be published using p*q is:',publickey_N)

print('Phi of N is',phi_n)
gcd(publickey_e,phi_n)
print('d:',privatekey_d)


print('Received N:',received_publicN)
print('Received e:',received_publickey)
print('decomposed received e:', receivedsquareandmul)

# Converting pre-defined Message and Signature to Int values      
Encryptionstring = conversionoftext('Marshall')
print(Encryptionstring)
SignedText = conversionoftext('Paul')
print(SignedText)
conversiontoint(Encryptionstring,SignedText)
print('Plain Text:',intequivalent)
print('Signature:',intequivalentsigned)

# Values to be used in Square and Multiply 

print('public key in power of 2s',squareandmul)


print('private key in power of 2s',smdecryption)


# Initiating RSA & RSA Signature

RSAfunc(received_publicN,received_publickey,
        privatekey_d,intequivalent,publickey_N)

backtooriginal(Decry)

Signedfunc(publickey_N, privatekey_d ,intequivalentsigned)

verification(received_publicN,received_publickey)

print('PlainText:',''.join(plaintextdecrypted))




    


        
    

