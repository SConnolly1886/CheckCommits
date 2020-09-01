"""
Read and parse the "From" lines and pull out the addresses from the line. Count the number
of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary.
Then sort the list in reverse order and print out the person who has
the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""
fname = input('Enter file name: ')
if len(fname) < 1 :
    fhandle = open('mbox-short.txt')
else:
    try:
        fhandle = open(fname)
    except:
        print('Invalid file')
        quit()

emails = {}
domains = {}

for line in fhandle:
    line = line.rstrip()
    line = line.split()
    if len(line) < 3 :
        continue
    if line[0] != 'From' :
        continue
    email = line[1]
    emails[email] = emails.get(email, 0) + 1
    uname, domain = email.split('@')
    #domain = email[atposition+1:]
    domains[domain] = domains.get(domain, 0) + 1

maxkey = None
maxvalue = None
minkey = None
minvalue = None
for key in emails :
    if maxkey is None or maxkey < emails[key] :
        maxkey = emails[key]
        maxvalue = key
    if minkey is None or minkey > emails[key] :
        minkey = emails[key]
        minvalue = key

countlist = []

for email, count in emails.items() :
    countlist.append((count, email))

countlist.sort(reverse=True)

for count, email in countlist[:1] :
    print(email, count)
