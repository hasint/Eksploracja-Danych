import Orange
data = Orange.data.Table("bridges")
print "%s" % ("Przykladowe instancje: ")
for x in data.domain.features:
    print "%-15s" % (x.name)

name = 'TYPE'
print "Lista wartosci zmiennej celu '%s'" % name
print data.domain[name].values
print "Histogram: \n"
print "brak"


print data.domain.features
m = len(data.domain.features)
m_cont = sum(1 for x in data.domain.features if x.var_type==Orange.feature.Type.Continuous)
m_disc = sum(1 for x in data.domain.features if x.var_type==Orange.feature.Type.Discrete)
c=""
d=""
for x in data.domain.features:
 if x.var_type==Orange.feature.Type.Continuous: c+=" " + x.name
 if x.var_type==Orange.feature.Type.Discrete: d+=" " + x.name
print "Atrybuty: \nWszystkich atrybutow: %d \n" % (m)
print "Atrybuty ciagle: %d, nazwy: %s \n" % (m_cont, c)
print "Atrybuty dyskretne: %d, nazwy: %s" % (m_disc, d)
average = lambda xs: sum(xs)/float(len(xs))

print "%-15s %s" % ("Atrybut", "Srednia")
for a in range(len(data.domain.attributes)):
   
        d = 0; n = 0
        for e in data:
            if not e[a].isSpecial():
                d += e[a]
                n += 1
        print "%s, %s, %3.2f" % (data.domain.attributes[a].name,"    ", d/n)

for x in data.domain.features:
    n_miss = sum(any(d[x].is_special() for x in data.domain.features) for d in data)
print "Liczba brakujacych elementow wszystkich atrybutow: %d" % n_miss
print "%-15s %s" % ("Atrybut", "Liczba brakujacych rekordow")
for x in data.domain.features:
	atr_miss = sum(d[x].is_special() for d in data)
	print "%-15s %.2f" % (x.name, atr_miss)
print "Przyklad trzech pierwszych probek: "
targets = data.domain.attributes
print "%s" % ( " ".join("%-5s" % c.name for c in targets))
for d in data[:3]:
    print "%-15s" % d
