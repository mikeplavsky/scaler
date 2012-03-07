#!/usr/bin/python

import boto
conn = boto.connect_autoscale()

from boto.ec2.autoscale import LaunchConfiguration

lc = LaunchConfiguration(
 
  name = 'phabricator', 
  image_id = 'ami-f0538e99',
  key_name = 'webserver',
  instance_type = 't1.micro',
  security_groups = ['default'] 

)

conn.create_launch_configuration( lc )

from boto.ec2.autoscale import AutoScalingGroup 

ag = AutoScalingGroup( 
  
  group_name = 'phabricator_fe',
  load_ballancers = ['phabricator'],
  availability_zones = ['us-east-1c','us-east-1d'],
  launch_config = lc,
  min_size = 2,
  max_size = 2

)

conn.create_auto_scaling_group( ag )
