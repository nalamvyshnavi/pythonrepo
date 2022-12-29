
import psutil
import time
UPDATE_DELAY=1
def get_size(bytes):
    for unit in ['','K','M','G','T','P']:
        if bytes<1024:
            return f"{bytes:.2f}{unit}B"
        bytes /=1024
        io=psutil.net_io_counters()
        bytes_sent,bytes_recv=io.bytes_sent,io.bytes_recv
while True:
    time.sleep(UPDATE_DELAY)
    io_2=psutil.net_io_counters()
    us,ds=io_2.bytes_sent,io_2.bytes_recv
    print(f" upload:{get_size(io_2.bytes_sent)}"
          f",Downolad:{get_size(io_2.bytes_recv)}"
          f",Upload speed:{get_size(us /UPDATE_DELAY)}/s"
          f",Downolad speed:{get_size(ds /UPDATE_DELAY)}/s",end="\r")
    bytes_sent,bytes_recv=io_2.bytes_sent,io_2.bytes_recv