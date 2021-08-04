import sys
import re
import pkg_resources

argg = sys.argv
argg.pop(0)

if len(argg) != 0:
  mlist = []
  mnames = []
  modulenames = []
  insmodule = []
  notinsmodule = []
  buinsmodule = []
  bmn = sys.builtin_module_names
  # Grab import module command
  for fname in argg:
    f = open(fname,'r').read().split('\n')
    ff = list(set(f[:15]))
    for fm in ff:
      if re.match('from', fm, re.IGNORECASE) or re.match('import', fm, re.IGNORECASE):
        mlist.append(fm)
      else:
        pass
  
  # Grabbing Module Name
  for o in mlist:
    if re.search('from', o, re.IGNORECASE):
      fx = re.sub(r'(?i)from ', '', o)
      mx = re.sub(r'(?i)import ', '', fx)
      mnames.append(mx)
    else:
      smx = re.sub(r'(?i)import ', '', o)
      mnames.append(smx)
  
  # Cleaning...
  for c in mnames:
    if c.count(' ') == 1:
      cname = c.split(' ')
      modulenames.append(cname[0])
    else:
      modulenames.append(c)
   
  print("Module's Name : ")
  for pkgd in modulenames:
    try:
      dist = pkg_resources.get_distribution(pkgd)
      insmodule.append(dist.key)
    except pkg_resources.DistributionNotFound:
      if pkgd in str(bmn):
        buinsmodule.append(pkgd)
      else:
        notinsmodule.append(pkgd)
  
  print("--------------")
  print("[•] Builtin Module [Installed] ")
  for u in buinsmodule:
    print("*. " + u)
  print("\n---------------------")
  print("[•] Installed Module : ")
  for v in insmodule:
    print("*. " + v)
  print("\n---------------------")
  print("[•] Not Istalled Module : ")
  for w in notinsmodule:
    print("*. " + w)

else:
  print('Give the argument..')
  print('~ python reqpip.py [Your Python Filename] [Another Python Filename] [Another Python Filename] [...]\n')
  print('For example : ')
  print('~ python reqpip.py test.py hello.py')