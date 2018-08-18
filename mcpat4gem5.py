#!/usr/bin/python2

from optparse import OptionParser
import json
import mako
import mcpat

def get_system_param(cfg):
    param = {}
    param['number_of_cores'] = len(cfg['system']['timingCPU'])
    param['target_core_clockrate'] = int(1000 / cfg['system']['clk_domain']['clock'][0])
    
    # core0
    param['core0']['clock_rate'] = int(1000 / cfg['system']['clk_domain']['clock'][0])
    param['core0']['vdd'] = cfg['system']['clk_domain']['voltage_domain']['voltage'][0]
    param['core0']['number_of_BTB'] = 1
    param['core0']['number_of_BPT'] = 1
    param['core0']['fetch_width'] =  cfg['system']['timingCPU']['fetchWidth']
    param['core0'][''] = 
    param['core0'] 
    param['core0'] 
    param['core0'] 
    param['core0'] 
    param['core0'] 
    return param

def get_system_stats():
    pass

if __name__ == "__main__":
    parser = OptionParser()

    parser.add_option("-c", "--config", dest="config",
                    help="gem5 full system configure file in json format" )
    parser.add_option("-s", "--stats", dest="stats",
                    help="gem5 status file in txt format")
    parser.add_option("-t", "--template", dest="template`",
                    help="Template xml file for McPAT")
    parser.add_option("--print_level", dest="plevel", default=0,
                    help="level of details 0~5")
    parser.add_option("--opt_for_clk", dest="opt_for_clk", default=1,
                    help="0:optimize for ED^2P only, 1:optimzed for target clock rate")

    (opts, args) = parser.parse_args()
    mcpat.cvar.opt_for_clk = bool(opts.opt_for_clk)

    system = {}
    with open(opts.config, 'r') as fp:
        cfg = json.load(fp)
   
    system.update(get_system_param(cfg))
    cfg.close()

    
    p1 = mcpat.ParseXML()
    p1.parse(opts.infile)

    proc = mcpat.Processor(p1)
    proc.displayEnergy(2, opts.plevel)

    exit(0)