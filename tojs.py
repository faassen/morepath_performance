# this generates two arrays that can be pasted into ``index.html`` as
# labels and data

all_rps = []
all_versions = []

with open('morepath_performance.txt', 'r') as f:
    for line in f:
        if not line.startswith('morepath'):
            continue
        parts = line.split()
        name, ms, rps, tcalls, funcs, version, date = parts
        all_rps.append(int(rps))
        all_versions.append(version)

print("var labels = %r;" % all_versions)
print("var data = %r;" % all_rps)
